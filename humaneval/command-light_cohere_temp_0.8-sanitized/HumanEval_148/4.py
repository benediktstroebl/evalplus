def bf(planet1, planet2):
    return [p for p in ['Earth', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Uranus'] if p in planet1 and p in planet2 and p <= (planet1 < planet2)]