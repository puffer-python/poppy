# poppy

This small lib is produced some functions to support convert string

## Setup

```commandline
pip install poppy
```

## Convert a string to Vietnamese without accents

```python
poppy.remove_accents('Xuân Hạ Thu Đông')  # Xuan Ha Thu Dong
```

## Generate Url Key

```python
poppy.generate_url_key('Xuan Ha thu Dong')  # xuan-ha-thu-dong
```