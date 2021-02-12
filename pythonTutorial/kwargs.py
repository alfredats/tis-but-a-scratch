def goodBurger(kind, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- We dont't have any", kind)
    print("-" * 40)
    print(keywords)


print(goodBurger( "Good Burger"
                , establishment="Good Burger"
                , motto="Welcome to Good Burger, Home of the Good Burger"
                ) )
