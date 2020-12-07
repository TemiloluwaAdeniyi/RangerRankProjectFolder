DATABASES = {
    'default': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': 'predictiondb',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}