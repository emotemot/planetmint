# Copyright © 2020 Interplanetary Database Association e.V.,
# Planetmint and IPDB software contributors.
# SPDX-License-Identifier: (Apache-2.0 AND CC-BY-4.0)
# Code is Apache-2.0 and docs are CC-BY-4.0

"""MongoDB backend implementation.

Contains a MongoDB-specific implementation of the
:mod:`~bigchaindb.backend.schema` and :mod:`~bigchaindb.backend.query` interfaces.

You can specify Planetmint to use MongoDB as its database backend by either
setting ``database.backend`` to ``'localmongodb'`` in your configuration file, or
setting the ``PLANETMINT_DATABASE_BACKEND`` environment variable to
``'localmongodb'``.

MongoDB is the default database backend for Planetmint.

If configured to use MongoDB, Planetmint will automatically return instances
of :class:`~bigchaindb.backend.localmongodb.LocalMongoDBConnection` for
:func:`~bigchaindb.backend.connection.connect` and dispatch calls of the
generic backend interfaces to the implementations in this module.
"""

# Register the single dispatched modules on import.
from planetmint.backend.localmongodb import schema, query # noqa

# MongoDBConnection should always be accessed via
# ``bigchaindb.backend.connect()``.
