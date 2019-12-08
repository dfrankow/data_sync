Introduction
------------

NOTE: This is unreleased software.  It's not done.

This is intended to be a simple implementation of synchronizing data
between two data sources with a "last write wins" policy.

I give no guarantee of correctness!  However, if it is correct, then
the result should be eventually consistent if peers synchronize with
each other regularly.

Currently, there are unchecked corner cases around concurrency.
For example, if one peer is synchronizing with two other peers at the
same time, that may not work, since there are multiple operations in
sync_both() and no transactional protection.

Tests
-----

To run tests:

```
$ docker-compose run data_sync nosetests sync_tests
```

You shouldn't have to give the "sync_tests", but
nosetests gets confused about the path.

To run tests and show logging from the `sync_tests` logger:

```
$ docker-compose run data_sync nosetests --debug=sync_tests sync_tests
```

See also [stackoverflow](https://stackoverflow.com/questions/32565562/make-nose-test-runner-show-logging-even-if-tests-pass).

To see the postgres DB:

```
$ docker-compose run db psql -h db -U postgres
```

To run the test server:

```
$ docker-compose run --service-ports data_sync env FLASK_APP=test_server.py flask run
```

Related efforts
---------------

There are many projects and concepts that relate to this type of data
syncing.

[SymmetricDS](https://symmetricds.org) is an open source project to synchronize
data.  However, a recent download of the server package is over 100M.
I hope this can be smaller and more nimble for my focused use case.

[CouchDB](https://couchdb.apache.org/) is another open source project to
synchronize data.  However, it requires the Erlang runtime, and implements
its own NoSQL document store.  I would like to have something I can use
with my common stack: Postgres on a server, and sqlite on android.

CouchDB has a nice property that every revision is always kept and
synced.  However, this makes querying more complicated, as you always
have to ignore old revisions.  Thus, I've decided to only keep the
latest revision ("last write wins"), which makes this effort not
compatible with CouchDB.

[Cloud Firestore](https://firebase.google.com/products/firestore/) is a
product that handles synchronization including an offline mode.  However,
it is a NoSQL data store.