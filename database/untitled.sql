

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: 'crud_flask'

CREATE TABLE IF NOT EXISTS 'interviewee' (
  'id' bigint NOT NULL,
  'emailID' varchar(255) NOT NULL,
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


INSERT INTO 'interviewee' ('id', 'emailID') VALUES
(1, 'malshikhareaditya@gmail.com');

ALTER TABLE 'interviewee'
  ADD PRIMARY KEY ('id');

ALTER TABLE 'interviewee'
  MODIFY 'id' bigint NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS 'interviewer' (
  'id' bigint NOT NULL,
  'emailID' varchar(255) NOT NULL,
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

INSERT INTO 'interviewer' ('id', 'emailID') VALUES
(1, 'vbnikam@vjti.ac.in');
ALTER TABLE 'interviewer'
  ADD PRIMARY KEY ('id');
ALTER TABLE 'interviewer'
  MODIFY 'id' bigint NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;


CREATE TABLE IF NOT EXISTS 'interview' (
'id' bigint NOT NULL,
'title' varchar(255) NOT NULL,
's_time' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
'e_time' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

INSERT INTO 'interview' ('id','title','s_time','e_time') VALUES
(1,'SDE Intern for InterviewBit',2018-04-04 10:00:00, 2018-04-04 13:00:00);
ALTER TABLE 'interview'
ADD PRIMARY KEY ('id');
ALTER TABLE 'interview'
MODIFY 'id' bigint NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;

create table if NOT EXISTS 'interviewer_assigned'
(interview_id bigint,
	interviewer_id bigint,
	foreign key(interview_id) references interview(id) on delete cascade,
	foreign key(interviewer_id) references interviewer(id) on delete cascade);

create table if NOT EXISTS 'interviewee_applied'
(interview_id bigint,
	interviewee_id bigint,
	foreign key(interview_id) references interview(id) on delete cascade,
	foreign key(interviewee_id) references interviewee(id) on delete cascade);
