# FOR REFERENCE ONLY

# python -m pip install --user --upgrade setuptools wheel twine
rm -rf bdist build pydotmap.egg-info dist
python setup.py sdist bdist_wheel
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# python -m twine upload  dist/*
