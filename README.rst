
.. note::

    This project does **not** require any GIS library or specific database.
    Map data are stored in simple JSON fields.

Install
=======

Install Django dependencies:

- create table in postgresql that you can change  table setting of setting.py
.. code-block:: bash

    pip install -r requirements.txt

Initialize database tables:

.. code-block:: bash

    python manage.py migrate

Create a super-user for the admin:

.. code-block:: bash

    python manage.py createsuperuser

Run
===

.. code-block:: bash

    python manage.py runserver

The map visible on http://127.0.0.1:8000/ can be edited from the AdminSite at ``/admin``.
