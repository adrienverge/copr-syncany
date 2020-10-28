copr-syncany
============

This repository provides unofficial packages for syncany, an open-source cloud
storage and filesharing application. 

From `Syncany homepage <https://www.syncany.org/>`_:

  Syncany allows users to securely backup and share certain folders of their
  computers using any kind of storage. Syncany is open-source and provides data
  encryption and incredible flexibility in terms of storage type and provider.

They are available for Fedora 22+ at:
https://copr.fedorainfracloud.org/coprs/adrienverge/syncany/

Installation
------------

.. code:: shell

 sudo dnf copr enable adrienverge/syncany
 sudo dnf install syncany

Hacking around
--------------

.. code:: shell

 rpmbuild -bs syncany.spec && \
 mock -r fedora-33-x86_64 \
      --enable-network \
      rebuild ~/rpmbuild/SRPMS/syncany-*.src.rpm
