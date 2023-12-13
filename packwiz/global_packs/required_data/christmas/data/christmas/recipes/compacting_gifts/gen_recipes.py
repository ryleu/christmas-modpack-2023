#!/usr/bin/env python3

import json

template = \
"""{{
    "type": "create:compacting",
    "ingredients": [
        {{
            "item": "minecraft:paper"
        }},
        {{
            "item": "minecraft:paper"
        }},
        {{
            "item": "minecraft:paper"
        }},
        {{
            "item": "minecraft:paper"
        }},
        {{
            "item": "minecraft:paper"
        }},
        {{
            "item": "minecraft:paper"
        }},
        {{
            "item": "minecraft:paper"
        }},
        {{
            "item": "minecraft:{color}_dye"
        }}
    ],
    "results": [
        {{
            "item": "winterly:{color}_gift_box"
        }}
    ]
}}"""

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "purple",
    "black",
    "white"
]

for color in colors:
    with open(f"gift_box_{color}.json", "w") as file:
        file.write(template.format(color=color))