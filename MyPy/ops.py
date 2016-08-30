from connect import connection
from time import sleep
class ops:
    def list(self,id):
        query='SELECT * FROM `user` WHERE `id`='+str(id)+';'
        obj=connection()
        while 1:
            if obj.lock.locked():
                obj.check.wait(1)
                obj.check.release()
            else:
                break
        obj.lock.acquire()
        obj.cc.execute(query)
        out=obj.cc.fetchone()
        obj.lock.release()
        #obj.cc.close()
        return(out)

    def add(self,email, passwd):
        task='INSERT INTO `user`(`email`,`password`) VALUES ('+'\"'+str(email)+'\"'+','+'\"'+str(passwd)+'\"'+');'
        obj=connection()
        while 1:
            if obj.lock.locked():
                sleep(1)
            else:
                break
        obj.lock.acquire()
        obj.cc.execute(task)
        obj.conn.commit()
        query='SELECT `id` FROM `user` WHERE `email`="'+email+'" AND `password`="'+passwd+'";'
        obj.cc.execute(query)
        sid=obj.cc.fetchone()
        print("The records are saved with id:%s\n" %sid['id'])
        obj.lock.release()
        #obj.conn.close()

