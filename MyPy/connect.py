import threading
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            #print("Inside if loop in Singelton")
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            #print("Singleton Triggers")
        return cls._instances[cls]
    def clear(cls):
        cls._instances={}
class connection():
    lock = threading.Lock()
    check = threading.Condition()
    pass
    import pymysql
    import pymysql.cursors
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read('config.ini')
    host = cfg.get('configs','url')
    user = cfg.get('configs','user')
    password = cfg.get('configs','passwd')
    db = cfg.get('configs','db')
    conn = pymysql.connect(host=host,user=user,password=password,db=db,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    cc = conn.cursor()

