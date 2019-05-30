'''
Created on 2019年5月21日

@author: bkd
'''
from os.path import join, expanduser
import sqlite3


class cmd():
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_file = join(expanduser("~"), ".config/kdCarCheckDevSimulator/kdCarCheckDevSimulator.db")
        self.id = None
    
    def add_cmd(self, model, value, remark, reply_type):
        conn = sqlite3.connect(self.db_file)
        cs = conn.cursor()
        cs.execute("insert into cmd (model,value,remark,reply_type) values(?,?,?,?)", (model, value, remark, reply_type))
        conn.commit()
        
    def delete_cmd(self, cmdId):
        self.run_sql("delete from cmd where id = '{}'".format(cmdId))

    def get_all(self, model):
        return self.run_sql("select id,model,value,remark,reply_type from cmd where model ='{}' order by remark".format(model))

    def modify_cmd(self):
        reply_type = 1
        if self.rb_random.isChecked():
            reply_type = 2
        self.run_sql("update cmd set  value ='{}', remark='{}', reply_type ='{}' where id='{}'".format(self.le_value.text(), self.le_remark.text(), reply_type, self.id))
    
    def run_sql(self, sql):    
        conn = sqlite3.connect(self.db_file)
        cs = conn.cursor()
        print("execute sql:" + sql)
        cs.execute(sql)
        if "select" in sql:
            return cs.fetchall()  
        conn.commit()
