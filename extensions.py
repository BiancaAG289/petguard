"""
extensions.py
--------------
Este archivo existe para inicializar aquí las extensiones de Flask
(como Flask-SQLAlchemy) en un solo lugar.

¿Por qué un archivo aparte?
Si `db` se define directamente en main.py, y models/models.py necesita
importar `db` desde main.py, se puede producir un "import circular"
(main.py importa de models.py, y models.py importa de main.py).

Al definir `db` aquí, tanto main.py como models/models.py pueden
importar desde extensions.py sin problema.

Todavía NO estamos usando base de datos en el MVP, así que este
archivo está preparado pero no activo todavía. Cuando lleguemos a
esa etapa, descomentaremos las siguientes líneas:

    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

Y en main.py se hará:

    from extensions import db
    db.init_app(app)
"""

# (vacío por ahora, a la espera de la etapa de base de datos)
