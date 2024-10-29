# local_settings.py

# Proje gizli anahtarını burada tanımlayın
SECRET_KEY = 'django-insecure-özel-bir-gizli-anahtar'

# Geliştirme ortamı için DEBUG modunu açık tutun
DEBUG = True

# Geliştirme sırasında tüm localhost bağlantılarına izin verin
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Veritabanı ayarları (MySQL kullanıyorsanız)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_pms',  # Veritabanı adı
        'HOST': '127.0.0.1',
        'USER': 'root',  # MySQL kullanıcı adı
        'PASSWORD': '',   # MySQL kullanıcı şifresi
    }
}
