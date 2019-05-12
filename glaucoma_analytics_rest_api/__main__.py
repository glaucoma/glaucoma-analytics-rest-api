from os import environ

from glaucoma_analytics_rest_api import routes, rest_api

_version = routes.__version__

rest_api.run(host=environ.get('HOST', '0.0.0.0'),
             port=environ.get('PORT', 5555),
             debug=bool(environ.get('DEBUG', True)))