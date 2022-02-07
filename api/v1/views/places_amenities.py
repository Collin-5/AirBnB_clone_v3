#!/usr/bin/python3
"""Amenities View"""


from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models import storage
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models import storage_t


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities(place_id):
    place = storage.get(Place, place_id)
    if place is not None:
        if storage_t == 'db':
            return jsonify([amenity.to_dict() for amenity in place.amenities])
        else:
            return jsonify([amenity.to_dict() for amenity in
                           place.amenity_ids])
    abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'],
                 strict_slashes=False)
def post_amenities(place_id, amenity_id):
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is not None and amenity is not None:
        if request.method == 'POST':
            if storage_t == 'db':
                place_amenities = place.amenities
            else:
                place_amenities = place.amenity_ids
            if amenity in place_amenities:
                return jsonify(amenity.to_dict())
            place_amenities.append(amenity)
            place.save()
            return make_response(jsonify(amenityto_dict()), 201)
    abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_amenities(place_id, amenity_id):
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is not None and amenity is not None:
        if storage_t == 'db':
            place_amenities = place.amenities
        else:
            place_amenities = place.amenity_ids
        if amenity not in place_amenities:
            abort(404)
        place_amenities.remove(amenity)
        place.save()
        return jsonify({})
    abort(404)
