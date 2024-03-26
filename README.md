# CNN Food Classifier

This repository contains code for training a Convolutional Neural Network (CNN) food classifier using Python. The classifier is trained using images from the Food-5K dataset and utilizes the VGG16 pre-trained network for feature extraction.

## Requirements

- Python 3.x
- TensorFlow
- scikit-learn
- NumPy
- imutils

## File Structure

- `train.py`: Script for training the logistic regression model using extracted features.
- `build_dataset.py`: Script for organizing the dataset into training, testing, and validation splits.
- `extract_features.py`: Script for extracting features from images using VGG16 and preparing data for training.
- `config.py`: Configuration file containing paths and constants used throughout the project.

## Usage

1. **Build Dataset**: Run `build_dataset.py` to organize the dataset into the desired splits (training, testing, and validation).

```bash
python build_dataset.py
```

2. **Extract Features**: Run `extract_features.py` to extract features from images using VGG16 and save them in CSV format along with labels.

```bash
python extract_features.py
```

3. **Train Model**: Finally, run `train.py` to train the logistic regression model using the extracted features.

```bash
python train.py
```

## Configuration

- `config.py` contains paths and constants used in the project. Adjust these paths if necessary.

## Output

- Trained model will be saved as `model.cpickle`.
- Label encoder will be saved as `le.cpickle`.
- Extracted features will be saved as CSV files in the `output` directory.

## Note

- Ensure that the Food-5K dataset is downloaded and placed in the appropriate directory (`Food-5K` by default).
- Modify the `config.py` file according to your dataset directory structure if different from the default.
- Additional configuration options such as batch size can be adjusted in `config.py`.
  
## Credits

This project utilizes the Food-5K dataset and the VGG16 pre-trained network. Credits to the authors of these resources.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
