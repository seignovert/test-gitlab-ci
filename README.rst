Gitlab CI Python to PyPi
=========================

Test and deploy Python package to PyPi with Gitlab CI/CD.

Run tests locally
-----------------

- Run ``tox`` with python 3.6:

.. code:: bash

    $ gitlab-runner exec docker py36

- Test deploy to Pypi:

.. code:: bash

    $ gitlab-runner exec docker pypi \
        --env PYPI_USERNAME=$PYPI_USERNAME \
        --env PYPI_PASSWORD=$(keyring get pypi $PYPI_USERNAME) \
        --env PYPI_URL=https://test.pypi.org/legacy/
