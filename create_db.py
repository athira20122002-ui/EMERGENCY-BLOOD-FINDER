import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "bloodbank.db")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()


c.execute("DROP TABLE IF EXISTS bloodbanks")


c.execute('''
CREATE TABLE bloodbanks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    address TEXT NOT NULL,
    phone TEXT NOT NULL,
    blood_groups TEXT NOT NULL
)
''')


c.execute('''
INSERT INTO bloodbanks (name, city, address, phone, blood_groups)
VALUES
('Pollachi Blood Bank Service & Diagnostic Laboratory', 'Pollachi', '30,palaniyammal layout, venketasha colony ', '99449 98898', 'All group available'),
('BioLine Laboratory', 'Pollachi', 'No.#38/2, G.R.Towers, New Scheme Rd, opp. to Karur Vysya Bank', 'N/A', 'All group available'),
('Government Hospital Blood Bank', 'Pollachi', 'Udumalai Pettai Road,', '04259 229 322', 'All group available'),
('Microbiological Laboratory', 'Pollachi', '34/4, Kamaraj Rd, Arumugam Nagar, Pollachi, Mahalingapuram', 'N/A', 'All group available')
''')

conn.commit()
conn.close()
print("Database created successfully!")
