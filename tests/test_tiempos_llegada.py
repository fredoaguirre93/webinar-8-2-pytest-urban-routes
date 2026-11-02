# Urban Routes — tiempo estimado de llegada
# tiempo (min) = distancia (km) / velocidad (km/h) * 60


def test_tiempo_viaje_corto():
    distancia = 6
    velocidad = 30
    tiempo = distancia / velocidad * 60
    assert tiempo == 12


def test_tiempo_viaje_largo():
    distancia = 20
    velocidad = 40
    tiempo = distancia / velocidad * 60
    assert tiempo == 30


def test_tiempo_hora_pico():
    distancia = 9
    velocidad = 18
    tiempo = distancia / velocidad * 60
    assert tiempo == 25


def test_tiempo_con_espera():
    distancia = 6
    velocidad = 30
    espera = 5
    tiempo = distancia / velocidad * 60 + espera
    assert tiempo == 17
