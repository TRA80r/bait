�
    �0�g�   �            
       ��   � d dl Z d dlZ e j                  dj                  dD � cg c]
  }  e| �      �� c} �      �        e j                  d�        ed ej                  �       j                  �       yc c} w )�    N� )�b   �a   �s   �h   �    �.   �t   �e   �r   �m   �u   �x   r	   r   r   �n   �clearzUnsupported CPU architecture:)�os�platform�system�join�chr�print�uname�machine)�is   0�bait.py�<module>r      s�   �� �9�2�9�9�R�W�W�  7B�  &C�  7B��c�!�f�  7B�  &C�  D�  E�  FO�  FH�  FO�  FO�  PW�  FX�  Y^�  _~�  M�  G�  M�  M�  O�  W�  W�  YX��  &Cs   �A3