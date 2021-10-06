from cassandra import Cluster

cluster = Cluster()
session = cluster.connect('killrvideo')
result = session.execute("SELECT * FROM users")[0]

for r in result:
    print(r)