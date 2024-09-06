
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

    try:
        planet1_index = {"Mercury":1, "Venus":2, "Earth":3, "Mars":4, "Jupiter":5, "Saturn":6, "Uranus":7, "Neptune":8}
        planet2_index = {"Mercury":1, "Venus":2, "Earth":3, "Mars":4, "Jupiter":5, "Saturn":6, "Uranus":7, "Neptune":8}
        if planet1 in planet1_index:
            planet1_index[planet1]
        if planet2 in planet2_index:
            planet2_index[planet2]
        planet1_index_pos = planet1_index[planet1]
        planet2_index_pos = planet2_index[planet2]
        planet_proximity = set()
        for planet in planet1_index_pos:
            if planet in planet2_index_pos:
                planet_proximity.add(planet)
        if len(planet_proximity)!= 0:
            planet_proximity
