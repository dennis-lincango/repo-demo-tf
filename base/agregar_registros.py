import sqlite3
import pandas as pd
import random

db_path = "base/viajes.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

ciudades_ecuador = [
    "Quito",         # Pichincha
    "Guayaquil",     # Guayas
    "Cuenca",        # Azuay
    "Loja",          # Loja
    "Ambato",        # Tungurahua
    "Manta",         # Manabí
    "Portoviejo",    # Manabí
    "Machala",       # El Oro
    "Esmeraldas",    # Esmeraldas
    "Riobamba",      # Chimborazo
    "Ibarra",        # Imbabura
    "Tulcán",        # Carchi
    "Latacunga",     # Cotopaxi
    "Babahoyo",      # Los Ríos
    "Tena",          # Napo
    "Puyo",          # Pastaza
    "Macas",         # Morona Santiago
    "Nueva Loja",    # Sucumbíos
    "Zamora",        # Zamora Chinchipe
    "Francisco de Orellana",  # Orellana
    "Santo Domingo", # Santo Domingo de los Tsáchilas
    "Santa Elena",   # Santa Elena
    "Azogues",       # Cañar
    "Milagro",       # Guayas
    "Quevedo",       # Los Ríos
    "Cayambe",       # Pichincha
    "Otavalo",       # Imbabura
    "Pelileo",       # Tungurahua
    "Salinas",       # Santa Elena
    "La Libertad"    # Santa Elena
]

df = pd.read_csv("data/personas.csv", sep="|", encoding="cp1252")
lista_personas = df["id_persona"].tolist()

def obtener_valor():

    valor = random.randint(100, 1000)
    return valor

def obtener_dias():

    valor = random.randint(1, 10)
    return valor

def obtener_ciudad():
    """
    """
    return ciudades_ecuador[random.randint(0, len(ciudades_ecuador)-1)]

# Insertar datos de ejemplo
viajes_data = []
for i in lista_personas:
    for j in range(0, 6):
        viajes_data.append((i, obtener_ciudad(), obtener_ciudad(), obtener_valor(), obtener_dias()))

print(len(viajes_data))
cursor.executemany("""
INSERT INTO viajes (id_persona, destino, origen, valor, dias_viaje)
VALUES (?, ?, ?, ?, ?);
""", viajes_data)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
