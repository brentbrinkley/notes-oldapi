class Scale:
    """
    Scale contains the different number of whole steps & half steps in each
    scale. It is used to query against our database to return a filtered
    notebank
    """

    scales = {
        "MAJOR": (2, 2, 1, 2, 2, 2, 1),
        "NATURAL_MINOR": (2, 1, 2, 2, 1, 2, 2),
        "MELODIC_MINOR": (2, 1, 2, 2, 2, 2, 1),
        "HARMONIC_MINOR": (2, 1, 2, 2, 1, 3, 2),
        "MAJOR_PENTATONIC": (2, 2, 3, 2, 3),
        "MINOR_PENTATONIC": (3, 2, 2, 3, 2),
        "BLUES": (3, 2, 1, 1, 3, 2),
        "IONIAN": (2, 2, 1, 2, 2, 2, 1),
        "DORIAN": (2, 1, 2, 2, 2, 1, 2),
        "PHRYGIAN": (1, 2, 2, 2, 1, 2, 2),
        "LYDIAN": (2, 2, 2, 1, 2, 2, 1),
        "MIXOLYDIAN": (2, 2, 1, 2, 2, 1, 2),
        "AEOLIAN": (2, 1, 2, 2, 1, 2, 2),
        "LOCRIAN": (1, 2, 2, 1, 2, 2, 2),
        "WHOLE_TONE": (2, 2, 2, 2, 2, 2),
        "WHOLE_HALF_DIM": (2, 1, 2, 1, 2, 1, 2, 1),
        "HALF_HOLE_DIM": (1, 2, 1, 2, 1, 2, 1, 2),
    }

    @classmethod
    def get_scale(cls, model, shape, key=""):
        base_note = model.query.filter_by(shape=shape).first().midi_val
        scale_container = []
        note_offset = 1

        for scale in cls.scales[key.upper()]:
            scale_container.append(model.query.get(base_note + note_offset).shape)
            base_note += scale

        return scale_container

