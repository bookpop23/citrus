import os
clientId = os.path.expandvars('$PGADMIN_AUTHENTIK_CLIENT_ID')
clientSecret = os.path.expandvars('$PGADMIN_AUTHENTIK_CLIENT_SECRET')

AUTHENTICATION_SOURCES = ['oauth2', 'internal']
OAUTH2_CONFIG = [
    {
        'OAUTH2_NAME': 'authentik',
        'OAUTH2_DISPLAY_NAME': 'authentik',
        'OAUTH2_CLIENT_ID': clientId,
        'OAUTH2_CLIENT_SECRET': clientSecret,
        'OAUTH2_TOKEN_URL': 'https://auth.reidsprite.com/application/o/token/',
        'OAUTH2_AUTHORIZATION_URL': 'https://auth.reidsprite.com/application/o/authorize/',
        'OAUTH2_API_BASE_URL': 'https://auth.reidsprite.com/',
        'OAUTH2_USERINFO_ENDPOINT': 'https://auth.reidsprite.com/application/o/userinfo/',
        'OAUTH2_SERVER_METADATA_URL': 'https://auth.reidsprite.com/application/o/pgadmin/.well-known/openid-configuration',
        'OAUTH2_SCOPE': 'openid email profile',
        'OAUTH2_ICON': 'fa-lock',
        'OAUTH2_BUTTON_COLOR': '#000000'
    }
]
OAUTH2_AUTO_CREATE_USER = True