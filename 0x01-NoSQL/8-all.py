#!/usr/bin/env python3
"""
Python function
"""


def list_all(mongo_collection):
    """
    show all documents in a collection.
    """
    arr_docs = []
    for doc in mongo_collection.find():
        arr_docs.append(doc)
    return arr_docs
