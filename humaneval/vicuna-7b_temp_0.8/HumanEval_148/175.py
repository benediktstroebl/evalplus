
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
    if not correct_planet_names(planet1, planet2):
        return ()
    
    #sorting by proximity to the sun
    return sorted((planet for planet in planets if planet.name != planet1 and planet.semi_major_axis < planet1.semi_major_axis), reverse=True)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planet1 = input("Enter the name of the planet with closest orbit to the sun: ")
planet2 = input("Enter the name of the planet with the orbit farthest from the sun: ")

print("Sorted planets: ", bf(planet1, planet2))