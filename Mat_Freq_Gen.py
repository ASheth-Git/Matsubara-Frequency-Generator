"""
Copyright 2024 Alpesh Rasikbhai SHETH

Licensed under the Apache License, Version 2.0 (the "License").
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# =============================================================================
# Matsubara Frequency Generator
# =============================================================================
import numpy as np

def matsubara_frequencies(beta, num_frequencies):
    """
    Generates Matsubara frequencies.

    Args:
        beta (float): The inverse temperature.
        num_frequencies (int): The number of frequencies to generate.

    Returns:
        ndarray: Array of Matsubara frequencies.
    """
    n_values = np.arange(0, num_frequencies)
    matsubara_freqs = np.pi / beta * (2 * n_values + 1) * 1j
    return matsubara_freqs
