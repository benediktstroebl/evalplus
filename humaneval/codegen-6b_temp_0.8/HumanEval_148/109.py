
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
    planets = (
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
        )
    
    def near_sun(angle):
        if angle < 280:
            return True
        else:
            return False
    
    def distance(planet1, planet2):
        angle = abs(reduce(
            operator.add,
            [
                orbital_motion(a, b)
                for a, b in ((planet1, "Sun"), (planet2, "Sun"))
                ]
            )
        )
        return angle if near_sun(angle) else 360 - angle
    
    def orbital_motion(planet1, planet2):
        if planet1 == planet2:
            return 0
        elif planet1 == "Sun":
            return orbital_motion("Sun", planet2)
        elif planet2 == "Sun":
            return orbital_motion(planet1, "Sun")
        else:
            angle = 2 * pi * (
                G * (masses[planet1] + masses[planet2]) /
                (distance(planet1, planet2) ** 2)
            )
            return angle
    
    masses = {
        planet: G * planet_mass(planet)
        for planet in planets
    }
    
    return tuple(sorted(
        planets,
        key=lambda planet: orbital_motion(planet1, planet2),
    ))
