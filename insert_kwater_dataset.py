import os
import csv
from util import string_list_to_list, list_to_dbarray
import psycopg2 as pg2


def read_csv_file(file_path):
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ", quotechar="|")

        vib = []
        for row in csvreader:
            vib.append(row[0])
        print(f"length: {len(vib)}")

    vib = list_to_dbarray(vib)
    return vib


def insert_into_db(acq_time, vib1, vib2, vib3, vib4, motor_id):
    try:
        with pg2.connect(
            "host = 10.10.30.17 dbname=rotor user=postgres password=1111 port=25433"
        ) as conn:
            with conn.cursor() as cur:  # 데이터 조회 쿼리 수정
                sql = f"insert into kwater.data (acq_time, motor_id, vib1, vib2, vib3, vib4) values ('{acq_time}', {motor_id}, {vib1}, {vib2}, {vib3}, {vib4})"
                cur.execute(sql)
            cur.close()
        conn.commit()
    except Exception as e:
        print(f"Error is {e}")
    else:
        pass
    finally:
        if conn:
            conn.close()
    pass


if __name__ == "__main__":
    # print(os.path.abspath(__file__))
    root_dir = "Z:\\3. 사업과제\\(2021) 수자원공사\\데이터_진동\\test_pump_vib"

    dirs = os.listdir(root_dir)
    for dir in dirs[15:]:
        dir_path = os.path.join(root_dir, dir)
        files = os.listdir(dir_path)
        for file in files:
            print(f'dir:{dir}, file:{file}')
            file_path = os.path.join(dir_path, file)

            if "Mod1ai0" in file:
                acq_time = (
                    file[0:4]
                    + "-"
                    + file[5:7]
                    + "-"
                    + file[8:10]
                    + " "
                    + file[11:13]
                    + ":"
                    + file[14:16]
                    + ":"
                    + file[17:19]
                )
                try:
                    vib1 = read_csv_file(file_path)
                except:
                    vib1 = []
            
            elif "Mod1ai1" in file:
                try:
                    vib2 = read_csv_file(file_path)
                except:
                    vib2 = []
            
            elif "Mod1ai2" in file:
                try:
                    vib3 = read_csv_file(file_path)
                except:
                    vib3 = []

            elif "Mod2ai0" in file:
                try:
                    vib4 = read_csv_file(file_path)
                except:
                    vib4 = []
                
                if len(vib1)==0 or len(vib2)==0 or len(vib3)==0 or len(vib4)==0:
                    pass
                else:
                    insert_into_db(acq_time, vib1, vib2, vib3, vib4, motor_id=1)

            elif "Mod2ai1" in file:
                acq_time = (
                    file[0:4]
                    + "-"
                    + file[5:7]
                    + "-"
                    + file[8:10]
                    + " "
                    + file[11:13]
                    + ":"
                    + file[14:16]
                    + ":"
                    + file[17:19]
                )
                try:
                    vib1 = read_csv_file(file_path)
                except:
                    vib1 = []

            elif "Mod2ai2" in file:
                try:
                    vib2 = read_csv_file(file_path)
                except:
                    vib2 = []

            elif "Mod3ai0" in file:
                try:
                    vib3 = read_csv_file(file_path)
                except:
                    vib3 = []

            elif "Mod3ai1" in file:
                try:
                    vib4 = read_csv_file(file_path)
                except:
                    vib4 = []
                
                if len(vib1)==0 or len(vib2)==0 or len(vib3)==0 or len(vib4)==0:
                    pass
                else:
                    insert_into_db(acq_time, vib1, vib2, vib3, vib4, motor_id=2)

            elif "Mod3ai2" in file:
                acq_time = (
                    file[0:4]
                    + "-"
                    + file[5:7]
                    + "-"
                    + file[8:10]
                    + " "
                    + file[11:13]
                    + ":"
                    + file[14:16]
                    + ":"
                    + file[17:19]
                )
                try:
                    vib1 = read_csv_file(file_path)
                except:
                    vib1 = []

            elif "Mod4ai0" in file:
                try:
                    vib2 = read_csv_file(file_path)
                except:
                    vib2 = []

            elif "Mod4ai1" in file:
                try:
                    vib3 = read_csv_file(file_path)
                except:
                    vib3 = []

            elif "Mod4ai2" in file:
                try:
                    vib4 = read_csv_file(file_path)
                except:
                    vib4 = []
                
                if len(vib1)==0 or len(vib2)==0 or len(vib3)==0 or len(vib4)==0:
                    pass
                else:
                    insert_into_db(acq_time, vib1, vib2, vib3, vib4, motor_id=3)

            elif "Mod5ai0" in file:
                acq_time = (
                    file[0:4]
                    + "-"
                    + file[5:7]
                    + "-"
                    + file[8:10]
                    + " "
                    + file[11:13]
                    + ":"
                    + file[14:16]
                    + ":"
                    + file[17:19]
                )
                try:
                    vib1 = read_csv_file(file_path)
                except:
                    vib1 = []

            elif "Mod5ai1" in file:
                try:
                    vib2 = read_csv_file(file_path)
                except:
                    vib2 = []

            elif "Mod5ai2" in file:
                try:
                    vib3 = read_csv_file(file_path)
                except:
                    vib3 = []

            elif "Mod6ai0" in file:
                try:
                    vib4 = read_csv_file(file_path)
                except:
                    vib4 = []
                
                if len(vib1)==0 or len(vib2)==0 or len(vib3)==0 or len(vib4)==0:
                    pass
                else:
                    insert_into_db(acq_time, vib1, vib2, vib3, vib4, motor_id=4)

            elif "Mod6ai1" in file:
                acq_time = (
                    file[0:4]
                    + "-"
                    + file[5:7]
                    + "-"
                    + file[8:10]
                    + " "
                    + file[11:13]
                    + ":"
                    + file[14:16]
                    + ":"
                    + file[17:19]
                )
                try:
                    vib1 = read_csv_file(file_path)
                except:
                    vib1 = []

            elif "Mod6ai2" in file:
                try:
                    vib2 = read_csv_file(file_path)
                except:
                    vib2 = []

            elif "Mod7ai0" in file:
                try:
                    vib3 = read_csv_file(file_path)
                except:
                    vib3 = []

            elif "Mod7ai1" in file:
                try:
                    vib4 = read_csv_file(file_path)
                except:
                    vib4 = []
                
                if len(vib1)==0 or len(vib2)==0 or len(vib3)==0 or len(vib4)==0:
                    pass
                else:
                    insert_into_db(acq_time, vib1, vib2, vib3, vib4, motor_id=5)

            elif "Mod7ai2" in file:
                acq_time = (
                    file[0:4]
                    + "-"
                    + file[5:7]
                    + "-"
                    + file[8:10]
                    + " "
                    + file[11:13]
                    + ":"
                    + file[14:16]
                    + ":"
                    + file[17:19]
                )
                try:
                    vib1 = read_csv_file(file_path)
                except:
                    vib1 = []

            elif "Mod8ai0" in file:
                try:
                    vib2 = read_csv_file(file_path)
                except:
                    vib2 = []

            elif "Mod8ai1" in file:
                try:
                    vib3 = read_csv_file(file_path)
                except:
                    vib3 = []

            elif "Mod8ai2" in file:
                try:
                    vib4 = read_csv_file(file_path)
                except:
                    vib4 = []
                
                if len(vib1)==0 or len(vib2)==0 or len(vib3)==0 or len(vib4)==0:
                    pass
                else:
                    insert_into_db(acq_time, vib1, vib2, vib3, vib4, motor_id=6)

            else:
                print('something error')
                pass
    
    print('done')