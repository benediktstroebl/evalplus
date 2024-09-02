
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    # Hint: you will need a few tuples to store all this info.
    # The easiest way is to make an array of all planets and loop through them.
    
    # Planets = ("Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    # planet1 = Planet.objects.get(name = planet1)
    # planet2 = Planet.objects.get(name = planet2)
    # orbit1 = planet1.orbit
    # orbit2 = planet2.orbit
    # planets = []
    # for planet in Planets:
    #     planet = Planet.objects.get(name = planet)
    #     if planet.orbit > orbit1 and planet.orbit < orbit2:
    #         planets.append(planet)
    # planets.sort(key = lambda x: x.orbit)
    # print planets
    # return planets
    
    # Most compact solution:
    Planets = ("Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    Planet1 = Planets.index(planet1)
    Planet2 = Planets.index(planet2)
    Planets = [s for s in Planets if s != planet1 and s != planet2]
    Planets.sort(key = lambda x: abs(Planet2 - Planets.index(x)))
    return tuple(Planets)

