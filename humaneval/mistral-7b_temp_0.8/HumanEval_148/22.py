
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

    #your code here

    # if either of the planet names are incorrect
    # raise a ValueError exception

    # declare a variable called planets that 
    # will contain a list of all of the planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # declare a variable called planets_between which will be an empty list
    # initially
    planets_between = []

    # declare a variable called index which will start off
    # with the index of planet1
    index = planets.index(planet1)

    # for each planet in planets
    for planet in planets:
        # if the index of the planet is greater than or equal to
        # the index of planet1 and the index of the planet is less 
        # than or equal to the index of planet2
        if index <= planets.index(planet) <= index + 1:
            # append the planet to planets_between
            planets_between.append(planet)

    # if neither of
