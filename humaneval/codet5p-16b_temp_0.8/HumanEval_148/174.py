
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

    def distance(p1, p2):
        if p1 == "Mercury" and p2 == "Venus":
            return 2.4
        elif p1 == "Venus" and p2 == "Earth":
            return 1.5
        elif p1 == "Earth" and p2 == "Mars":
            return 2.5
        elif p1 == "Mars" and p2 == "Jupiter":
            return 5.2
        elif p1 == "Jupiter" and p2 == "Saturn":
            return 9.7
        elif p1 == "Saturn" and p2 == "Uranus":
            return 28.7
        elif p1 == "Uranus" and p2 == "Neptune":
            return 50.5
        else:
            return 1000000

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_dict = {}

    for p in planets:
        planet_dict[p] = distance(planet1
