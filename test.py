from pydotmap import DotMap


author = DotMap(name="atul", sirname="singh", addr=[{"country": "India"}])
print(author.name)
print(author.sirname)
del author.sirname
print(author.sirname)
print(author.get("sirname", "singh"))  # you can use your default value same as dict
print(author.addr[0].country)
