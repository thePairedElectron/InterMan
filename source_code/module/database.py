import pymysql

class Database:
    def connect(self):
        return pymysql.connect("localhost","root","root","crud_flask" )
    
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try: 
            if id == None:
                cursor.execute("SELECT i.id,i.title,DATE(i.s_time), TIME(i.s_time),TIME(e_time),(SELECT emailID from interviewee where id=ie.interviewee_id),(SELECT emailID from interviewer where id=ia.interviewer_id) FROM interview i join interviewer_assigned ia on i.id=ia.interview_id join interviewer ir on ia.interviewer_id=ir.id join interviewee_applied ie on i.id=ie.interview_id join interviewee iv on ie.interviewee_id=iv.id")
            else: 
                cursor.execute("SELECT * FROM interview i join interviewer_assigned ia on i.id=ia.interview_id join interviewer ir on ia.interviewer_id=ir.id join interviewee_applied ie on i.id=ie.interview_id join interviewee iv on ie.interviewee_id=iv.id and DATE(i.s_time)= %s ",(id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
            
    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        # title=data['title']
        # print title
        # stri=data['doi']
        # mm,dd,yyyy=stri.split("/")
        # string=yyyy+mm+dd+" "
        # iptime1=data['start_time']
        # hh,temp=iptime1.split(":")
        # ii,mode=temp.split(" ")
        # if mode == "AM":
        #     string2=hh+":"+ii+":"+":00"
        # else:
        #     string2=(hh+12)+":"+ii+":"+":00"
        # print string2
        # string=data['doi']+" "+data['start_time']
        # string2=data['doi']+" "+data['end_time']

        # print string
        # print string2
        try:
            cursor.execute("INSERT INTO interview(title,s_time,e_time) VALUES(%s, %s, %s)", (data['title'],(data['doi']+" "+data['start_time']),(data["doi"]+" "+data['end_time']),))
            # print "1"
            cursor.execute("INSERT INTO interviewee(emailID) VALUES(%s)", (data['interviewee_email']))
            # print "2"
            cursor.execute("INSERT INTO interviewer(emailID) VALUES(%s)", (data['interviewer1_email']))
            # print "3"
            cursor.execute("INSERT INTO interviewer(emailID) VALUES(%s)", (data['interviewer2_email']))
            # print "4"
            cursor.execute("INSERT INTO interviewer(emailID) VALUES(%s)", (data['interviewer3_email']))
            # print "5"
            cursor.execute("INSERT INTO interviewer(emailID) VALUES(%s)", (data['interviewer4_email']))
            # print "6"
            cursor.execute("INSERT INTO interviewer_assigned(interview_id,interviewer_id) VALUES(SELECT id from interview where title=%s,SELECT id from interviewer where emailID=%s", (data['title'],data['interviewer1_email'],))
            # print "7"
            cursor.execute("INSERT INTO interviewee_applied(interview_id,interviewee_id) VALUES(SELECT id from interview where title=%s,SELECT id from interviewee where emailID=%s", (data['title'],data['interviewee_email'],))
            # print "8"
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
            
    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("UPDATE interview set title = %s, s_time = %s, e_time = %s where id = %s", (data['title'],data['doi']+" "+data['start_time'],data['doi']+" "+data['end_time'],id,))
            cursor.execute("UPDATE interviewee set emailID = %s where id = %s",(data['interviewee_email'],id,))
            cursor.execute("UPDATE interviewer set emailID = %s where id = %s",(data['interviewer1_email'],id,))
            cursor.execute("UPDATE interviewer set emailID = %s where id= %s",(data['interviewee_email'],id,))
            cursor.execute("UPDATE interviewee set emailID = %s where id = %s",(data['interviewee_email'],id,))
            cursor.execute("UPDATE interviewee_applied set interview_id = (SELECT id from interview where title = %s) and interviewee_id = (SELECT id from inteviewee where emailID= %s)",(data['title'],data['interviewee_email'],))
            cursor.execute("UPDATE interviewer_assigned set interview_id = (SELECT id from interview where title = %s) and interviewer_id = (SELECT id from inteviewer where emailID= %s)",(data['title'],data['interviewer1_email'],))
            cursor.execute("UPDATE interviewer_assigned set interview_id = (SELECT id from interview where title = %s) and interviewer_id = (SELECT id from inteviewer where emailID= %s)",(data['title'],data['interviewer2_email'],))
            cursor.execute("UPDATE interviewer_assigned set interview_id = (SELECT id from interview where title = %s) and interviewer_id = (SELECT id from inteviewer where emailID= %s)",(data['title'],data['interviewer3_email'],))
            cursor.execute("UPDATE interviewer_assigned set interview_id = (SELECT id from interview where title = %s) and interviewer_id = (SELECT id from inteviewer where emailID= %s)",(data['title'],data['interviewer4_email'],))

            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()
        
    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM interview where id = %s", (id,))
            con.commit()
            
            return True
        except:
            con.rollback()
            
            return False
        finally:
            con.close()