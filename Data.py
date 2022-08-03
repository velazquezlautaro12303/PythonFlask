"""\
    Este modulo sera utilizado para proporcionar los informacion de los tweet desde una base de datos.
"""

Comment0 = """W3Schools is optimized for learning, testing, and 
            training. Examples might be simplified to improve 
            reading and basic understanding. Tutorials, references,
            and examples are constantly reviewed to avoid errors,
            but we cannot warrant full correctness of all content.
            While using this site, you agree to have read and
            accepted our terms of use, cookie and privacy
            policy.Copyright 1999-2022 by Refsnes Data. All Rights
            Reserved."""

Comment1 = """What can Python do?
            Python can be used on a server to create web applications.
            Python can be used alongside software to create workflows.
            Python can connect to database systems. It can also read and modify files.
            Python can be used to handle big data and perform complex mathematics.
            Python can be used for rapid prototyping, or for production-ready software development.
            """

Comment2 = """Why Python?    
            Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
            Python has a simple syntax similar to the English language.
            Python has syntax that allows developers to write programs with fewer 
            lines than some other programming languages.
            Python runs on an interpreter system, meaning that code can be executed as soon as it is written. 
            This means that prototyping can be very quick.
            Python can be treated in a procedural way, an object-oriented way or a functional way.
            """

Comment3 = """Good to know
            The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, 
            although not being updated with anything other than security updates, is still quite popular.
            In this tutorial Python will be written in a text editor. 
            It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse 
            which are particularly useful when managing larger collections of Python files.
            """

Comment4 = """Python Syntax compared to other programming languages
            Python was designed for readability, and has some similarities 
            to the English language with influence from mathematics.
            Python uses new lines to complete a command, as opposed to other programming languages 
            which often use semicolons or parentheses.
            Python relies on indentation, using whitespace, to define scope; such as the scope of loops, 
            functions and classes. Other programming languages often use curly-brackets for this purpose.
            """

import sqlobject as SO
import datetime
from sqlobject.inheritance import InheritableSQLObject

# driver//user/password@localhost/nameDataBase
__connection__ = SO.connectionForURI("mysql://root:murcielago456@localhost/newDataBase")


class TweetInstagram:
    def __init__(self, name_user, datetime, description, comment, likes, path_photos):
        """
        Esta clase sera utlizada para almacenar la
        informacion de los tweets desde la base de datos
        :param name_user: nombre de usuario
        :param datetime: fecha y hora
        :param description: description del tweet
        :param count_share: cantidad de veces, que se compartio el tweet
        :param count_comment: cantidad de comentarios
        :param count_likes: cantidad de Me gusta al tweet
        :param path_photo: path de photos/imagenes del tweet
        """
        self.nameUser = name_user
        self.dateTime = datetime
        self.description = description
        # self.share = share
        self.comment = comment
        self.likes = likes
        self.pathPhotos = path_photos


class User(SO.SQLObject):
    nameUser = SO.UnicodeCol(length=120, varchar=True, notNone=True)


class PathPhoto(SO.SQLObject):
    path = SO.UnicodeCol(length=250, varchar=True, notNone=True)
    tweet = SO.ForeignKey("PostInstagram", default=None, notNone=False)


class Likes(SO.SQLObject):
    userDidLike = SO.ForeignKey("User", default=None, notNone=True)
    tweet = SO.ForeignKey("PostInstagram", default=None, notNone=False)


class Comment(SO.SQLObject):
    comment = SO.UnicodeCol(length=120, varchar=True, notNone=True)
    userDidComment = SO.ForeignKey("User", default=None, notNone=True)
    tweet = SO.ForeignKey("PostInstagram", default=None, notNone=False)


class PostInstagram(SO.SQLObject):
    description = SO.UnicodeCol(length=600, varchar=True, notNone=True)
    datetime = SO.UnicodeCol(length=50, varchar=True, notNone=True)
    nameUser = SO.ForeignKey("User", default=None, notNone=True)


# if __name__ == '__main__':
if __name__ == '__main__':

    # Borro la tabla si existe
    Comment.dropTable(ifExists=True, cascade=True)
    Likes.dropTable(ifExists=True, cascade=True)
    PathPhoto.dropTable(ifExists=True, cascade=True)
    PostInstagram.dropTable(ifExists=True, cascade=True)
    User.dropTable(ifExists=True, cascade=True)

    # __connection__.queryAll("truncate table path_photo")
    # __connection__.queryAll("truncate table post_instagram")
    # __connection__.queryAll("truncate user")
    # __connection__.queryAll("truncate table comment")
    # __connection__.queryAll("truncate table likes")

    # Creo las tablas
    User.createTable()
    PostInstagram.createTable()
    PathPhoto.createTable()
    Likes.createTable()
    Comment.createTable()

    user1 = User(nameUser="Velazquez Lautaro")
    user2 = User(nameUser="Maily Chalco")
    user3 = User(nameUser="Abril Cotta")
    user4 = User(nameUser="Gabriel Quiroz")

    post1 = PostInstagram(description="Alan invertirá el dinero de Walden en la colección de ropa de Kate. Walden,"
                                      " por su lado está comenzando a ver lo difícil que es mantener una doble vida.",
                          datetime=str(datetime.datetime.now()),
                          nameUser=user1)

    post2 = PostInstagram(description="En este capítulo, Walden, Alan, Billy y Herb se reunirán para compartir sus "
                                      "historias acerca de las mujeres que han pasado por sus vidas.",
                          datetime=str(datetime.datetime.now()),
                          nameUser=user3)

    post3 = PostInstagram(description="Durante un evento para solteros, Walden se encontrará con su exesposa y todo "
                                      "parece apuntar a una reconciliación. Alan, sin embargo, "
                                      "se preocupará por el futuro de ambos.", datetime=str(datetime.datetime.now()),
                          nameUser=user4)

    post4 = PostInstagram(description="Luego de una fuerte discusión con Walden, Alan decide dejar la mansión "
                                      "de Malibú e irse a vivir con Herb.", datetime=str(datetime.datetime.now()),
                          nameUser=user2)

    post5 = PostInstagram(description="Alan la pasará muy mal cuando Lyndsey termine con él.",
                          datetime=str(datetime.datetime.now()),
                          nameUser=user4)

    PathPhoto(path="../static/imagen/farmer.png", tweet=post1)
    PathPhoto(path="../static/imagen/carpenter.png", tweet=post2)
    PathPhoto(path="../static/imagen/baker.png", tweet=post3)
    PathPhoto(path="../static/imagen/electrician.png", tweet=post4)
    PathPhoto(path="../static/imagen/mayor.png", tweet=post5)

    Comment(comment="Alto farmer", userDidComment=user2, tweet=post1)

    Likes(userDidLike=user3, tweet=post1)
    Likes(userDidLike=user4, tweet=post1)

    # #############################################################

tweets = []
for post in PostInstagram.select():
    path_photos = []
    for photo in PathPhoto.select(PathPhoto.q.tweet == post):
        path_photos.append(photo.path)
    user_likes = []
    for like in Likes.select(Likes.q.tweet == post):
        user_likes.append(like.userDidLike.nameUser)
    comments = []
    for comment in Comment.select(Comment.q.tweet == post):
        comments.append((comment.comment, comment.userDidComment.nameUser))

    tweet = TweetInstagram(name_user=post.nameUser.nameUser, datetime=post.datetime, description=post.description,
                           comment=comments, likes=user_likes, path_photos=path_photos)

    tweets.append(tweet)

