# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_mthreads_ml_py_lifecycle_version_is_required():
    requirements = (ROOT / "requirements" / "common.txt").read_text().splitlines()

    assert "mthreads-ml-py>=2.4.3" in requirements
