Gitlab CI Python to PyPi
=========================

|Build| |Coverage| |PyPI| |Version| |License|

.. |Build| image:: https://gitlab.com/seignovert/test-gitlab-ci/badges/master/pipeline.svg
        :target: https://gitlab.com/seignovert/test-gitlab-ci/pipelines
.. |Coverage| image:: https://gitlab.com/seignovert/test-gitlab-ci/badges/master/coverage.svg
        :target: https://gitlab.com/seignovert/test-gitlab-ci/commits/master
.. |PyPI| image:: https://img.shields.io/badge/dynamic/json.svg?label=PyPI%20(test)&url=https%3A%2F%2Ftest.pypi.org%2Fpypi%2Ffoo-gitlab-ci%2Fjson&query=info.name&colorB=blue
        :target: https://test.pypi.org/project/foo-gitlab-ci
.. |Version| image:: https://img.shields.io/badge/dynamic/json.svg?label=Version&url=https%3A%2F%2Ftest.pypi.org%2Fpypi%2Ffoo-gitlab-ci%2Fjson&query=info.version&colorB=orange
        :target: https://test.pypi.org/project/foo-gitlab-ci
.. |License| image:: https://img.shields.io/badge/dynamic/json.svg?label=License&url=https%3A%2F%2Ftest.pypi.org%2Fpypi%2Ffoo-gitlab-ci%2Fjson&query=info.license&colorB=green
        :target: https://test.pypi.org/project/foo-gitlab-ci

Test and deploy Python package to PyPi with Gitlab CI/CD.

Run tests locally
-----------------

- Run ``tox`` with python 3.6:

.. code:: bash

    $ gitlab-runner exec docker py36

- Test deploy to PyPI:

.. code:: bash

    $ gitlab-runner exec docker pypi \
        --env PYPI_USERNAME=$PYPI_USERNAME \
        --env PYPI_PASSWORD=$(keyring get pypi $PYPI_USERNAME) \
        --env PYPI_URL=https://test.pypi.org/legacy/
