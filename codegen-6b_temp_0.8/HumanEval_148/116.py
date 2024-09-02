
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
    # Hint: you can use len(planets) to get the number of planets in
    #       the list, and the index for the current planet being checked 
    #       in planets.
    planets = (
        "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
    )
    planet1 = planet1.lower()
    planet2 = planet2.lower()

    if planet1 not in planets or planet2 not in planets:
        return tuple()
    elif planet1 == planet2:
        return tuple(sorted([planet1]))

    for planet in planets:
        if planets.index(planet) < planets.index(planet1) < planets.index(planet2):
            return tuple(sorted([planet1, planet2]))

assert bf("Saturn", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
assert bf("Venus", "Jupiter") == ("Mercury", "Earth", "Mars", "Jupiter", "Saturn")
assert bf("Neptune", "Earth") == ("Venus", "Mars", "Jupiter", "Saturn", "Uranus")
assert bf("Mercury", "Venus") == ("Earth")
assert bf("Mercury", "Venus") == ("Earth", "Mercury")
assert bf("Venus", "Mercury") == ("Mercury")
assert bf("Jupiter", "Mercury") == ("Mercury", "Jupiter")
assert bf("Jupiter", "Saturn") == ("Mercury", "Jupiter", "Saturn")
assert bf("Saturn", "Uranus") == ("Mercury", "Jupiter", "Saturn")
assert bf("Saturn", "Uranus") == ()
assert bf("Uranus", "Neptune") == ("Saturn", "Uranus")
assert bf("Earth", "Neptune") == ("Venus", "Mars", "Jupiter", "Saturn", "Uranus")
assert bf("Earth", "Neptune") == ("Venus", "Mars", "J