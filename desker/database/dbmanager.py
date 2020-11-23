# CRUD for desker database
import sqlite3


class ManageDB:
    def create_db_connection(db_file):
        """Creates a connection to a database

        Args:
            db_file ([type]): [db file location]
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(
                f"Connection to database {db_file} created.", sqlite3.version)
        except sqlite3.Error as error:
            print(error)
        finally:
            if conn:
                conn.close()

    def create_table_user_apps(db_file):

        conn = None
        try:
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS userApps")
            query = """CREATE TABLE userApps(
                    ID INT PRIMARY KEY NOT NULL,
                    appName TEXT NOT NULL UNIQUE, 
                    location TEXT NOT NULL UNIQUE, 
                    numTimesOpened INT NOT NULL )"""
            cursor.execute(query)
            conn.commit()
            print("Database table created successfully.")
        except sqlite3.Error as error:
            print("Error occurred while creating table userApps", error)
        finally:
            if conn:
                conn.close()


class Setters:
    def insert_new_app(id, app_name, app_location):
        """Inserts new default app in the database.

        Args:
            id ([int]): [New app ID, should be incremental],
            app_name ([string]): [App name in the system],
            app_location ([string]): [Location of the app executable]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            query = ('INSERT INTO userApps (ID,appName,location,numTimesOpened) '
                     'VALUES (:ID, :appName, :location, :numTimesOpened);')
            params = {
                'ID': id,
                'appName': app_name,
                'location': app_location,
                'numTimesOpened': 1
            }
            conn.execute(query, params)
            conn.commit()
            cursor = conn.execute(f"SELECT * from userApps")
            print("Successfully inserted new app into userApps")
            return cursor.fetchall()

        except sqlite3.Error as error:
            print("Failed to insert new app into userApps", error)
        finally:
            if (conn):
                conn.close()


class Getters:
    def get_all_apps(self):
        """Obtains all information about the apps in the Database

        Returns:
            [list]: [All information about all the apps]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            cursor = conn.execute(f"SELECT * from userApps")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to read data from userApps", error)
        finally:
            if (conn):
                conn.close()

    def get_app_by_id(id):
        """Obtains all information about the app passed by id

        Args:
            id ([int]): [App ID]

        Returns:
            [list]: [App Info]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            cursor = conn.execute(f"SELECT * from userApps WHERE ID={id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to read data from userApps", error)
        finally:
            if (conn):
                conn.close()

    def get_app_name_by_id(id):
        """Obtains the name of the app passed by id

        Args:
            id ([int]): [App ID]

        Returns:
            [list]: [Name of the app]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            cursor = conn.execute(
                f"SELECT appName from userApps WHERE ID={id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to read data from userApps", error)
        finally:
            if (conn):
                conn.close()

    def get_app_location_by_id(id):
        """Obtains the app location of the app passed by id

        Args:
            id ([int]): [App ID]

        Returns:
            [list]: [Location of the app]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            cursor = conn.execute(
                f"SELECT location from userApps WHERE ID={id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to read data from userApps", error)
        finally:
            if (conn):
                conn.close()

    def get_app_num_times_opened_by_id(id):
        """Obtains the number of times the app passed by id was opened

        Args:
            id ([int]): [App ID]

        Returns:
            [list]: [Number of times opened]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            cursor = conn.execute(
                f"SELECT numTimesOpened from userApps WHERE ID={id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to read data from userApps", error)
        finally:
            if (conn):
                conn.close()


class Updaters:
    def update_app_name(id, app_name):
        """Update the name of the app with the ID passed as argument.

        Args:
            id ([int]): [ID of the app to update]
            app_name ([string]): [Name to update the app with]

        Returns:
            [list]: [Information of the app updated]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            conn.execute(
                f"UPDATE userApps SET appName = '{app_name}'' WHERE ID = {id}")
            conn.commit()
            cursor = conn.execute(f"SELECT * FROM userApps WHERE ID = {id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to update data from userApps", error)
        finally:
            if (conn):
                conn.close()

    def update_app_location(id, app_location):
        """Update the location of the app with the ID passed as argument.

        Args:
            id ([int]): [ID of the app to update]
            app_location ([string]): [location to update the app with]

        Returns:
            [list]: [Information of the app updated]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            conn.execute(
                f"UPDATE userApps SET location = '{app_location}'' WHERE ID = {id}")
            conn.commit()
            cursor = conn.execute(f"SELECT * FROM userApps WHERE ID = {id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to update data from userApps", error)
        finally:
            if (conn):
                conn.close()

    def update_app_nums_time_opened(id, num_times_opened):
        """Update the number of times the app was opened with the app ID passed as argument.

        Args:
            id ([int]): [ID of the app to update]
            num_times_opened ([string]): [location to update the app with]

        Returns:
            [list]: [Information of the app updated]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            conn.execute(
                f"UPDATE userApps SET numTimesOpened = '{num_times_opened}'' WHERE ID = {id}")
            conn.commit()
            cursor = conn.execute(f"SELECT * FROM userApps WHERE ID = {id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to update data from userApps", error)
        finally:
            if (conn):
                conn.close()


class Removers:
    def remove_app_by_id(id):
        """Removes app from database with the ID passed as argument.

        Args:
            id ([int]): [ID of the app to remove.]

        Returns:
            [list]: [Updated data from the Database]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            conn.execute(f"DELETE from userApps where ID = {id};")
            conn.commit()
            cursor = conn.execute("SELECT * from userApps")
            print(f"App with id {id} was removed successfully")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Error occurred while deleting data from userApps", error)
        finally:
            if (conn):
                conn.close()
