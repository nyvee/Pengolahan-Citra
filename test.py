import glob
import ultralytics
from ultralytics import YOLO
from IPython.display import Image, display

# Perform Ultralytics checks
ultralytics.checks()

# Load the model
model = YOLO('yolo11n.pt')

# Train the model
train_dir = 'runs/detect/train'  # Fixed directory name
model.train(data='datasets/data.yaml', epochs=100, imgsz=640, project='runs/detect', name='train', exist_ok=True)

# Display training results
display(Image(filename=f'{train_dir}/confusion_matrix.png', width=900))
display(Image(filename=f'{train_dir}/results.png', width=900))

# Paths
model_path = f'{train_dir}/weights/best.pt'
data_path = 'datasets/data.yaml'
test_path = 'datasets/test/images'

# Validate the model
results = YOLO(model_path).val(data=data_path, project='runs/detect', name='val', exist_ok=True)
print("Validation Results:")
print(results)

# Predict using the model
predict_dir = 'runs/detect/predict'
results = YOLO(model_path).predict(source=test_path, save=True, project='runs/detect', name='predict', exist_ok=True)

# Display predictions
for image_path in glob.glob(f'{predict_dir}/*.jpg')[:5]:
    display(Image(filename=image_path, width=300))
    print("\n")