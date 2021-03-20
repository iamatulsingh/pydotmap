from pydotmap import DotMap
from pydotmap import OrderedDotMap
from pydotmap import dotmap, ordered_dotmap


author = DotMap(name="atul", sirname="singh", addr=[{"country": "India"}])
print(author.name)
print(author.sirname)
del author.sirname
print(author.sirname)
print(author.get("sirname", "singh"))  # you can use your default value same as dict
print(author.addr[0].country)


# Oderdered Map - This will maintain the order of your dictionary

author = OrderedDotMap(name="atul", sirname="singh", addr=[{"country": "India"}])
print(author)

value = {"author": "atul"}


@dotmap
def check_dotmap_decorator(in_value):
    return in_value.author

print(check_dotmap_decorator(value))


@ordered_dotmap
def check_orderedmap_decorator(in_value):
    return in_value.author

print(check_orderedmap_decorator(value))