#!/bin/env python3

template = \
"""{{
    "type": "minecraft:crafting_shaped",
    "pattern": [
        "G#S"
    ],
    "key": {{
        "G": {{
            "item": "minecraft:glowstone"
        }},
        "#": {{
            "item": "minecraft:{ingredient}"
        }},
        "S": {{
            "item": "minecraft:string"
        }}
    }},
    "result": {{
        "item": "snowyspirit:glow_lights_{variety}",
        "count": 16
    }}
}}"""

colors = [
    ("red_dye", "red"),
    ("orange_dye", "orange"),
    ("yellow_dye", "yellow"),
    ("green_dye", "green"),
    ("blue_dye", "blue"),
    ("purple_dye", "purple"),
    ("magenta_dye", "magenta"),
    ("light_blue_dye", "light_blue"),
    ("cyan_dye", "cyan"),
    ("lime_dye", "lime"),
    ("brown_dye", "brown"),
    ("black_dye", "black"),
    ("white_dye", "white"),
    ("pink_dye", "pink"),
    ("gray_dye", "gray"),
    ("light_gray_dye", "light_gray"),
    ("diamond", "prismatic")
]

for i in colors:
    with open(f"glow_lights_{i[1]}.json", "w") as file:
        file.write(template.format(ingredient=i[0], variety=i[1]))
