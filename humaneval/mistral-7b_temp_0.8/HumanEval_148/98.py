
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
    # planets_info = {"Mercury": "Mercury is the smallest planet in the Solar System",
    #                 "Venus": "Venus is the second planet from the Sun and is sometimes called Earth's 'twin'",
    #                 "Earth": "Earth is the third planet from the Sun and is sometimes called Earth's 'twin'",
    #                 "Mars": "Mars is the fourth planet from the Sun and is sometimes called Earth's 'twin'",
    #                 "Jupiter": "Jupiter is the largest planet in the Solar System",
    #                 "Saturn": "Saturn is the second largest planet in the Solar System",
    #                 "Uranus": "Uranus is the third largest planet in the Solar System",
    #                 "Neptune": "Neptune is the fourth largest planet in the Solar System"}
    # planets_info = {"Mercury": 36000000,
    #                 "Venus": 67000000,
    #                 "Earth": 1490000
