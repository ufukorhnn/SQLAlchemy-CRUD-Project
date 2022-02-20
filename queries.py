from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist


engine = create_engine("Insert Your Database Path", echo=True)


# create a Session
Session = sessionmaker(bind=engine)
session = Session()


# how to do a SELECT * (All)
res = session.query(Artist).all()
count =1
for artist in res:
    print(f"{count}- {artist.name}")
    count +=1

# how to SELECT the first result
res = session.query(Artist).filter(Artist.name=="Newsboys").first()

# how to sort the result (ORDER_BY)
res = session.query(Album).order_by(Album.title).all()
for album in res:
    print(album.title)

# how to do JOINed query 
qry = session.query(Artist,Album)
qry = qry.filter(Artist.id==Album.artist_id)
artist, album = qry.filter(Album.title=="Step Up to the Microphone").first()

# how to use LIKE in a query
res = session.query(Album).filter(Album.publisher.like("S%a%")).all()
for item in res:
    print(item.publisher)