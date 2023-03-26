# 0x09. Web infrastructure design

## Requirements
## General
* A README.md file, at the root of the folder of the project, is mandatory
* For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
* This project will be manually reviewed:
* As each task is completed, the name of that task will turn green
* Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use imgur but feel free to use anything you want).
* For the following tasks, insert the link from of your screenshot into the answer file
* After pushing your answer file to GitHub, insert the GitHub file link into the URL box
* You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
* Focus on what you are being asked:
* Cover what the requirements mention, we will explore details in a later project
* Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
* Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
* In this project, again, avoid going in details if not asked



For the task 0, my answers
• What is a server
A server is a piece of computer hardware or software that provide services to other computers called clients. The services include data sharing, web page rendering, mail provision e.t.c. The various kinds of servers include web servers, file servers, application servers, database servers e.t.c.
• What is the role of the domain name
The domain name is to enable a particular server's location to be easily remembered, it identifies a server's numerical IP address with a human-readable name
• What type of DNS record www is in www.foobar.com
It is an A record, it translates foobar.com to it's corresponding IP address
• What is the role of the web server
A web server is a piece of software on a dedicated hardware that facilitates serving of web pages to client devices. It serves up the static content of a page
• What is the role of the application server
Application server delivers business application to client dynamically, with the use of Application Programmable Interfaces (APIs), the contents are readily available to software developers
• What is the role of the database
The databases allow multiple users at the same time to quickly and securely access and query the data using highly complex logic and language. (Source: https://www.oracle.com/ke/database/what-is-database/)
• What is the server using to communicate with the computer of the user requesting the website
It uses HTTP protocols for communication
The issues with this infrastructure
• SPOF
Multiple infrastructure do not exist, so if one infrastructure goes down, services to the client will be automatically interrupted
• Downtime when maintenance needed (like deploying new code web server needs to be restarted)
	When deploying new code, the server has to be temporarily unavailable which would cause service unavailability
	• Cannot scale if too much incoming traffic
	There are not multiple servers that can distribute load, this infrastructure cannot handle too much incoming tra



For task 1:
• For every additional element, why you are adding it
Load balancer:
• This was added to reduce the work-load on individual servers.
• To enable concurrent use of multiple servers which boosts efficiency
• It makes the servers respond more quickly which helps boost performance
• Single point of failure is reduced. When one server fails, the active one provides availability
A second server
• To reduce the single point of failure (SPOF)
	• To maximise availability and minimise downtime
	• What distribution algorithm your load balancer is configured with and how it works
	Round robin: it passes each new connection request to the next server in line, eventually distributing connections evenly across the array of servers being load balanced
	• Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
	It is enabling an active-active setup
	In the active-active peer setup, both servers are actively handling user requests concurrently, while in the active-passive setup, only one server is active and the other one is passive or standby and only becomes effective when the active server fails
	• How a database Primary-Replica (Master-Slave) cluster works
	Master-slave replication enables data from one database server (the master) to be replicated to one or more other database servers (the slaves). The master logs the updates, which is effected on the slave. There is synchronous and asynchronous Replication.
	• What is the difference between the Primary node and the Replica node in regard to the application
	The primary node is the node that receives all write operation from the client application, it logs the updates received. The Replica node has an instance of the updates received from the primary node
	• You must be able to explain what the issues are with this infrastructure:
	• Where are SPOF
	• The dns server
	• The load balancer
	• Security issues (no firewall, no HTTPS)
	• Since there is no firewall, incoming and outgoing traffic cannot be monitored and intrusion detection is not possible
	• The communication is also nor secure as no HTTPS is used, therefore hackers can intercept and collect information about the client's traffic
	• No monitoring
	The state of each server cannot be known since there's no monitoring


Task 2
09:27
Additional Elements and Their Purpose:
Firewalls: The three firewalls are added to provide an additional layer of security and protect the infrastructure from unauthorized access and cyber-attacks.
SSL Certificate: The SSL certificate is added to serve www.foobar.com over HTTPS, which encrypts the communication between the server and the client and prevents any eavesdropping or data interception.
Monitoring Clients: The three monitoring clients are added to collect data and provide real-time information about the infrastructure's health and performance.
Why Firewalls are Needed:
Firewalls are needed to secure the infrastructure and protect it from unauthorized access and cyber-attacks. They help to filter traffic and prevent malicious traffic from reaching the servers, which reduces the risk of a security breach.
Why Traffic is Served over HTTPS:
HTTPS is used to encrypt the communication between the server and the client, which prevents any eavesdropping or data interception. It also helps to establish the authenticity of the website and provides assurance that the website is legitimate and not a fake site created by hackers to steal sensitive information.
Why Monitoring is Used:
Monitoring is used to provide real-time information about the infrastructure's health and performance. It helps to detect and fix any issues or errors 

before they become critical, which reduces downtime and ensures that the website is always available and running smoothly.
How Monitoring Tool is Collecting Data:
The monitoring tool collects data by installing agents on the servers, which collect and send data to the monitoring client. The monitoring client then aggregates and analyzes the data, which is displayed on a dashboard for real-time monitoring.
Monitoring Web Server QPS:
To monitor web server QPS (queries per second), we can use a monitoring tool that can track web server metrics such as CPU usage, memory usage, and network traffic. By analyzing these metrics, we can determine the web server QPS and identify any performance bottlenecks.
Issues with This Infrastructure:
Terminating SSL at the load balancer level is an issue because it reduces the security of the infrastructure. If the SSL certificate is terminated at the load balancer level, the communication between the load balancer and the servers is not encrypted, which increases the risk of data interception and cyber-attacks.
Having only one MySQL server capable of accepting writes is an issue because it creates a single point of failure. If the MySQL server fails, the website will not be able to accept any writes, which can lead to data loss and downtime.
Having servers with all the same components (database, web server, and application server) might be a problem because it increases the risk of a single

Task 3

The last task:
Specifics About This Infrastructure
• The addition of a firewall between each server ensures high security for each server
Issues With This infrastructure:
The cost of maintenance is high
