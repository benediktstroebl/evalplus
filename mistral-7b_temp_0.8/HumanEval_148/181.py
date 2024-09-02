
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
    # Orbit in order: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
    # Neptune is the furthest planet from the sun

    # Helper function to find the distance between two planets
    # use the orbital period as a proxy for distance
    # The orbital period is the time that it takes a planet to orbit the sun
    # The orbital periods of the planets are:
    # Mercury: 0.2408467 years
    # Venus: 0.61519726 years
    # Earth: 1.00000000 years
    # Mars: 1.8808158 years
    # Jupiter: 11.862615 years
    # Saturn: 29.447498 years
    # Uranus: 84.016846 years
    # Neptune: 164.79132 years
    def dist(planet1, planet2):
        per
