
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

    import itertools
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    planet1, planet2 = planet1.lower(), planet2.lower()
    try:
        for planet in planets:
            if planet1!= planet and planet2!= planet:
                raise ValueError
        if planet1 == planet2:
            raise ValueError
    except ValueError:
        print("Enter correct planet names")
    else:
        if planet1 == "mercury" or planet2 == "mercury":
            result = planets[:4]
        elif planet1 == "venus" or planet2 == "venus":
            result = planets[4:8]
        elif planet1 == "earth" or planet2 == "earth":
            result = planets[8:12]
        elif planet1 == "mars" or planet2 == "mars":
            result = planets[12:16]
        elif planet1 == "jupiter" or planet2 == "jupiter":
