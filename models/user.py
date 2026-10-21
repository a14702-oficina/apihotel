from con_sql_alchemy import bd

class HotelModel(bd.Model):
    __tablename__ = "utilizadores"
    user_id = bd.Column(bd.String, primary_key= True)
    username = bd.Column(bd.String(40))
    passsword = bd.Column(bd.String(40))

    def __init__(self, username, passsword):
        self.username = username
        self.passsword = passsword

    def json(self):
        return {
            "user_id": self.user_id, 
            "username": self.username
            }

    @classmethod
    def find_user(cls, username):
        user = cls.query.filter_by(username = username).first()
        if user:
            return user
        return None

    def save_user(self):
        bd.session.add(self)
        bd.session.commit()

    def update_user(self, username,passsword):
        self.username = username
        self.passsword = passsword


    def delete_user(self):
        bd.session.delete(self)
        bd.session.commit()