
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
    orbital_elements = {
        "Sun": [0, 0, 0, 0, 0, 0], 
        "Mercury": [0, 4.481368, 0, 0, 0, 0], 
        "Venus": [0, 10.30323, 0, 0, 0, 0],
        "Earth": [0, 12.0192, 0, 0, 1, 0],
        "Mars": [0, 19.7979, 0, 1, 0, 0],
        "Jupiter": [0, 30.0601, 1, 0, 0, 0],
        "Saturn": [0, 39.5479, 0, 1, 0, 0.58],
        "Uranus": [0, 45.2647, 0, 1, 0.186, 0.959],
        "Neptune": [0, 48.866, 0, 1, 0.051, 0.299]
        }
        
    def planet_id(planet):
        return orbital_elements[planet][5]

    def calculate_angle(planet1, planet2):
        x = planet_id(planet1) - planet_id(planet2)
        return math.atan2(x, orbital_elements[planet1][4] - orbital_elements[planet2][4])

    def calculate_distance(planet1, planet2):
        y = orbital_elements[planet1][4] - orbital_elements[planet2][4]
        x = orbital_elements[planet1][5] - orbital_elements[planet2][5]
        return math.sqrt(y**2 + x**2)

    tuple_out = tuple([planet for planet in orbital_elements if planet_id(planet) > planet_id(planet1) and planet_id(planet) < planet_id(planet2)])
    return tuple_out
