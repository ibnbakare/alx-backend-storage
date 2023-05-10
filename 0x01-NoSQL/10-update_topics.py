#!/usr/bin/env python3
"""
Task 10
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes topics in the colection
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
