import numpy as np
import os
import sys

sys.path.append(os.getcwd())
from automlToolkit.components.meta_learning.meta_features import calculate_all_metafeatures
from automlToolkit.components.utils.constants import MULTICLASS_CLS, REGRESSION

np.random.seed(1)
X = np.random.rand(100, 5)
# y = np.array([np.random.randint(5) for _ in range(100)])
y = np.random.rand(100)
meta = calculate_all_metafeatures(X=X,
                                  y=y,
                                  task_type=REGRESSION,  # MULTICLASS_CLS
                                  categorical=[False] * 5,  # Categorical mask, list of bool
                                  dataset_name="default")
print(meta.load_values())
