from sqlalchemy import create_engine, text

db_con_str = "mysql+pymysql://at4byfeu6jk77gzlijg3:pscale_pw_vuC2TVDeiucLwiC5WTkotxk2xZpLBAT6JQgaxvrQDP5@aws.connect.psdb.cloud/mijnwebsite?charset=utf8mb4"

engine = create_engine(db_con_str, 
      connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())