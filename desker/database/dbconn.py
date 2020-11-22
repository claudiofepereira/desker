# CRUD for userApps module
import sqlite3


class Setters:
    def insert_new_app(id, appName, location):
        """Inserts new default app in the database.

        Args:
            id ([int]): [New app ID, should be incremental],
            appName ([string]): [App name in the system],
            location ([string]): [Location of the app executable]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            query = ('INSERT INTO userApps (ID,appName,location,numTimesOpened) '
                     'VALUES (:ID, :appName, :location, :numTimesOpened);')
            params = {
                'ID': id,
                'appName': appName,
                'location': location,
                'numTimesOpened': 1
            }
            conn.execute(query, params)
            conn.commit()
            print("Successfully inserted new app into userApps")
        except sqlite3.Error as error:
            print("Failed to insert new app into userApps", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")


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
                print("sqlite connection is closed")

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
                print("sqlite connection is closed")

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
                print("sqlite connection is closed")

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
                print("sqlite connection is closed")

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
                print("sqlite connection is closed")


class Updaters:
    def update_app_name(id, appName):
        """Update the name of the app with the ID passed as argument.

        Args:
            id ([int]): [ID of the app to update]
            appName ([string]): [Name to update the app with]

        Returns:
            [list]: [Information of the app updated]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            conn.execute(
                f"UPDATE userApps SET appName = '{appName}'' WHERE ID = {id}")
            conn.commit()
            cursor = conn.execute(f"SELECT * FROM userApps WHERE ID = {id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to update data from userApps", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")

    def update_app_location(id, location):
        """Update the location of the app with the ID passed as argument.

        Args:
            id ([int]): [ID of the app to update]
            location ([string]): [location to update the app with]

        Returns:
            [list]: [Information of the app updated]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            conn.execute(
                f"UPDATE userApps SET location = '{location}'' WHERE ID = {id}")
            conn.commit()
            cursor = conn.execute(f"SELECT * FROM userApps WHERE ID = {id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to update data from userApps", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")

    def update_app_nums_time_opened(id, numTimesOpened):
        """Update the location of the app with the ID passed as argument.

        Args:
            id ([int]): [ID of the app to update]
            location ([string]): [location to update the app with]

        Returns:
            [list]: [Information of the app updated]
        """
        conn = None
        try:
            conn = sqlite3.connect('desker.db')
            conn.execute(
                f"UPDATE userApps SET numTimesOpened = '{numTimesOpened}'' WHERE ID = {id}")
            conn.commit()
            cursor = conn.execute(f"SELECT * FROM userApps WHERE ID = {id}")
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Failed to update data from userApps", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")


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
            return cursor.fetchall()
        except sqlite3.Error as error:
            print("Error occurred while deleting data from userApps", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
