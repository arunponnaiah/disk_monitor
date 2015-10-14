#! /usr/bin/env python
import os, math , datetime
PARTITIONS=('/')
THRESHOLD=90
print 'starting at ' , datetime.datetime.now()
for partition in PARTITIONS:
 result  = os.statvfs(str(partition)) 
 free = result.f_frsize * result.f_bavail
 total = result.f_frsize * result.f_blocks
 disk_result = ( float( free)/total ) * 100
 print 'disk_result :',disk_result
 if disk_result >= THRESHOLD:
  print "disk usage is ",disk_result ,"Time to clean up!!!"
print 'End at ' , datetime.datetime.now()
