# injection-attacks-demo
Injection attack allows an attacker to inject code into a program or query or inject malware onto a computer in order to execute remote commands that can read or modify a database, or change data on a web site.

This is a very basic web app that demonstrates SQL, code and cross-site scripting(xss) injection attacks.

For Code injection, in enter your name form:
Normal input : your_name
Attack input : <p style="background-color:red;font-size:35pt;">your_name</p>

For xss injection, in enter your name form:
Input: <script> alert("HACKED") </script>

For SQL injection, in search bar on next page:
Normal i/p : rice (shows items named rice)
Attack i/p : rice' UNION SELECT username,password from employees;--
(Exposes the username and password of the employees)
