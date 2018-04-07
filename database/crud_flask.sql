

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS interviewee(
  id bigint AUTO_INCREMENT,
  emailID varchar(255),
  primary key(id)
);

ALTER TABLE interviewee AUTO_INCREMENT=1;

INSERT INTO interviewee (emailID) VALUES
('malshikhareaditya@gmail.com');



CREATE TABLE IF NOT EXISTS interviewer (
  id bigint,
  emailID varchar(255), primary key(id)
);

ALTER TABLE interviewer AUTO_INCREMENT=1;
INSERT INTO interviewer (emailID) VALUES
('vbnikam@vjti.ac.in');



CREATE TABLE IF NOT EXISTS interview (
id bigint,
title varchar(255),
s_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
e_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
primary key(id)
);

ALTER TABLE interview AUTO_INCREMENT=1;
INSERT INTO interview (title,s_time,e_time) VALUES
('SDE Intern for InterviewBit','2018-04-04 10:00:00', '2018-04-04 13:00:00');

create table if NOT EXISTS interviewer_assigned
(interview_id bigint,
	interviewer_id bigint,
	foreign key(interview_id) references interview(id) on delete cascade,
	foreign key(interviewer_id) references interviewer(id) on delete cascade);

create table if NOT EXISTS interviewee_applied
(interview_id bigint,
	interviewee_id bigint,
	foreign key(interview_id) references interview(id) on delete cascade,
	foreign key(interviewee_id) references interviewee(id) on delete cascade);
