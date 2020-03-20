import models.note_model as model


def main():
    """Builds our database with the proper values"""

    COLORS = [
        "gold",
        "black",
        "red",
        "orange",
        "yellow",
        "green",
        "cyan",
        "blue",
        "purple",
        "pink",
        "grey",
    ]

    SHAPES = [
        "circle",
        "moon",
        "star",
        "plus",
        "triangle",
        "square",
        "key",
        "leaf",
        "crown",
        "cube",
        "minus",
        "sun",
    ]

    HEX = [
        "#4A4A4A",
        "#A49085",
        "#E14A39",
        "#FB9F26",
        "#FBC51D",
        "#60BB6C",
        "#56ABD4",
        "#2B82C9",
        "#9464BA",
        "#ED6689",
        "#D8D8D8",
    ]

    OCTAVES = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    PITCHES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    COMMON_NOTATION = [f"{pitch}{octave}" for octave in OCTAVES for pitch in PITCHES]

    SVG_PATHS = [
        "M86.603 0l86.602 50v100l-86.602 50L0 150V50L86.603 0zm.058 129.362c16.17 0 29.28-13.108 29.28-29.278 0-16.17-13.11-29.28-29.28-29.28s-29.277 13.11-29.277 29.28 13.108 29.278 29.278 29.278z",
        "M87.512 0l86.602 50v100l-86.602 50L.91 150V50L87.51 0zM66.01 124.795c4.4 2.685 9.57 4.232 15.1 4.232 16.032 0 29.027-12.996 29.027-29.027 0-16.03-12.995-29.027-29.027-29.027-5.53 0-10.7 1.547-15.1 4.232C74.36 80.302 79.936 89.5 79.936 100c0 10.5-5.575 19.698-13.926 24.795z",
        "M87.42 0l86.603 50v100L87.42 200 .82 150V50L87.42 0zm9.677 122.857l12.437-1.102.884-12.454 8.015-9.572-8.18-9.432-1.102-12.437-12.454-.885-9.573-8.015-9.432 8.18-12.435 1.102-.885 12.455-8.015 9.573 8.18 9.432 1.103 12.436 12.454.885 9.573 8.015 9.432-8.18z",
        "M76.41 89H61.917c-2.21 0-4.01 1.795-4.01 4.01v13.98c0 2.21 1.796 4.01 4.01 4.01h14.49v14.49c0 2.212 1.796 4.01 4.01 4.01H94.4c2.21 0 4.01-1.795 4.01-4.01V111h14.49c2.21 0 4.01-1.795 4.01-4.01V93.01c0-2.21-1.796-4.01-4.01-4.01H98.41V74.51c0-2.212-1.796-4.01-4.01-4.01H80.42c-2.21 0-4.01 1.795-4.01 4.01V89zM87.33 0l86.602 50v100L87.33 200 .727 150V50L87.33 0z",
        "M87.24 0l86.6 50v100l-86.6 50L.635 150V50L87.24 0zm-.02 68.582L54.585 121.98h65.27L87.22 68.582z",
        "M87.148 0l86.603 50v100L87.15 200 .545 150V50L87.148 0zM66.455 73.322c-3.32 0-6.01 2.69-6.01 6.01v41.504c0 3.32 2.69 6.01 6.01 6.01h41.503c3.32 0 6.01-2.69 6.01-6.01V79.332c0-3.32-2.69-6.01-6.01-6.01H66.455z",
        "M87.057 0l86.603 50v100l-86.603 50L.455 150V50L87.057 0zm-8.85 97.583l-7.68 27.565c-.59 2.118.714 3.852 2.918 3.852h28.02c2.204 0 3.51-1.725 2.916-3.852l-7.677-27.565c5.242-2.69 8.752-7.597 8.752-13.198 0-8.49-8.066-15.385-18-15.385-9.935 0-18 6.894-18 15.385 0 5.6 3.51 10.507 8.75 13.198z",
        "M105.268 80.712c-.734 1.864-2.6 3.187-4.785 3.187-2.827 0-5.12-2.217-5.12-4.95 0-2.094 1.345-3.884 3.245-4.607-2.82-2.426-5.723-4.644-8.452-6.558-8.592 6.025-18.903 15.06-22.912 24.098-5.73 12.05-5.73 24.097 0 30.122 5.04 5.302 14.52 5.938 20.626 2.688-.012.106-.016.214-.014.323l.188 7.105h4.55l-.188-7.104c-.004-.123-.016-.244-.037-.362 6.1 3.294 15.636 2.674 20.698-2.65 5.728-6.024 5.728-18.072 0-30.12-1.685-3.8-4.484-7.597-7.8-11.172zM86.966 0l86.603 50v100l-86.604 50L.364 150V50L86.966 0z",
        "M86.875 0l86.603 50v100l-86.603 50L.273 150V50L86.875 0zm25.5 87.736c0 2.025.982 3.79 2.46 4.79-3.122 4.684-7.527 10.122-12.067 11.697-5.975 2.075-11.545-10.676-14.287-18.254 2.034-.765 3.514-2.853 3.514-5.328 0-3.114-2.323-5.642-5.185-5.642-2.857 0-5.183 2.528-5.183 5.642 0 2.475 1.478 4.56 3.513 5.327-2.735 7.577-8.3 20.328-14.284 18.253-4.534-1.575-8.948-7.013-12.063-11.696 1.47-1.002 2.455-2.763 2.455-4.79 0-3.115-2.328-5.646-5.19-5.646-2.857 0-5.183 2.532-5.183 5.646 0 3.123 2.326 5.65 5.182 5.65.06 0 7.156 32.49 7.156 32.49h47.2l7.006-32.51c3.01.02 5.335-2.507 5.335-5.63-.003-3.114-2.328-5.645-5.182-5.645-2.87 0-5.197 2.532-5.197 5.646z",
        "M86.784 0l86.603 50v100l-86.603 50L.182 150V50L86.784 0zm-.102 66l-29.5 17.032v34.063l29.5 17.032 29.5-17.032V83.032L86.682 66z",
        "M86.693 0l86.603 50v100l-86.603 50L.09 150V50L86.694 0zM61.085 86c-3.31 0-5.994 2.693-5.994 6.004v15.044c0 3.316 2.694 6.004 5.995 6.004h50.232c3.31 0 5.994-2.693 5.994-6.004V92.004c0-3.316-2.693-6.004-5.993-6.004H61.085z",
        "M86.603 0l86.602 50v100l-86.602 50L0 150V50L86.603 0zm-.365 127.197l6.945 10.686 2.612-12.47 10.34 7.457-2.073-12.572 12.338 3.222-6.48-10.974 12.67-1.45-10.008-7.894 11.29-5.923-12.187-3.75 8.386-9.6-12.72.903 4.35-11.977-11.534 5.432-.275-12.738-8.79 9.23L86.237 63l-4.862 11.78-8.792-9.23-.274 12.738-11.536-5.432 4.35 11.977-12.72-.902 8.386 9.6-12.187 3.75 11.29 5.922-10.01 7.895 12.67 1.45-6.478 10.973 12.338-3.222-2.073 12.572 10.34-7.458 2.612 12.47 6.946-10.685z",
    ]

    counter = 0

    for index_1, color in enumerate(COLORS):
        for index_2, shape in enumerate(SHAPES):
            if counter <= 127:
                model.Note.create(
                    color=color,
                    shape=shape,
                    midi_val=counter,
                    common_notation=COMMON_NOTATION[counter],
                    hex=HEX[index_1],
                    svg=SVG_PATHS[index_2],
                )

            counter += 1


if __name__ == "__main__":
    model.initialize_db()
    main()
